<template>
    <div class="logincontainer">
        <el-form class="loginForm" :model="loginForm" ref="loginForm" :inline="false" size="normal" :rules="rules">
            <el-form-item>
                <div class="loginTitle">
                    系统登录
                </div>
            </el-form-item>

            <el-form-item prop="username">
                <el-input v-model="loginForm.username" placeholder="用户名"></el-input>
            </el-form-item>
            <el-form-item prop="password">
                <el-input type="password" v-model="loginForm.password" placeholder="密码"></el-input>
            </el-form-item>

            <el-form-item prop="code">
                <el-row :gutter="20">
                    <el-col :span="16" :offset="0">
                        <el-input v-model="loginForm.code" placeholder="输入验证码"></el-input>
                    </el-col>
                    <el-col :span="8" :offset="0">
                        <el-input v-model="loginForm.code" placeholder="验证码"></el-input>
                    </el-col>
                </el-row>
            </el-form-item>
            <el-form-item >
                <el-row :gutter="20">
                    <el-col :span="12" :offset="0">
                        <el-button @click="handerLogin" class="btn" type="primary" size="default">登录</el-button>
                    </el-col>
                    <el-col :span="12" :offset="0">
                        <el-button class="btn" type="default" size="default">注册</el-button>
                    </el-col>
                </el-row>

            </el-form-item>

        </el-form>

    </div>
</template>

<script>
export default {
    //存储数据，页面显示的地方都需要显示在data里面定义
    //双向绑定
    data() {
        return {
            //登录数据域
            loginForm: {
                username: '',
                password: '',
                code: '',
            },
            //表单数据域
            rules: {
                username: [
                    {
                        required: true,
                        trigger: 'change',
                        message: '请输入用户名'

                    }
                ],
                password: [
                    {
                        required: true,
                        trigger: 'change',
                        message: '请输入密码'
                    }
                ],
                code: [
                    {
                        required: true,
                        trigger: 'change',
                        message: '请输入验证码'
                    }
                ]
            }
        };

    },
    methods: {
        //登录提交事件

        handerLogin() {
            this.$refs.loginForm.validate(valid=>{
                if(valid){
                    console.log('验证通过')
                }
            })
        }
    }

};
</script>

<style lang="scss" scoped>
.logincontainer {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;

    .loginForm {
        height: 350px;
        width: 450px;
        box-shadow: 0 0 25px #cac6c6;
        border-radius: 10px;
        padding: 20px 35px;

        .loginTitle {
            font-size: 18px;
            font-weight: 600;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .btn {
            width: 100%;

        }


    }
}
</style>